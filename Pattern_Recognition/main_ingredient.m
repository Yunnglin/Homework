%%���ɷַ��� 
%https://jingyan.baidu.com/article/e75aca85307fb5142edac6c6.html
%https://blog.csdn.net/qq_25800311/article/details/83385029
load data.mat
%coeff�Ǹ������ɷֵ�ϵ��Ҳ����ת������score�Ǹ������ɷֵĵ÷֣�latent��X������ֵ��tsquare��ÿ�����ݵ�ͳ��ֵ
all_feature = [train_feature;test_feature];
[coeff,score,latent,tsquare]=pca(all_feature);
contribution = (100*latent./sum(latent));
cumsum(latent)./sum(latent)
%%
pca_train_feature = score(1:600,1:20);
pca_test_feature = score(601:1860,1:20);
%%
train_fe=pca_train_feature(1:500,:);
train_la =  train_label(1:500,:);
test_fe = pca_train_feature(501:600,:);
test_la =  train_label(501:600,:);
[bestacc,bestc,bestg] = SVMcgForClass(train_la,train_fe,-2,4,-4,4,3,0.5,0.5,0.9);
%ѵ��ģ��
cmd = ['-c ',num2str(bestc),' -g ',num2str(bestg)];
 model = svmtrain(train_la,train_fe, cmd);
 test_label = round(rand(1260,1)*10);
 [predicted_label,accuracy,n] = svmpredict(test_la, test_fe, model,'-q');
 %%
 [bestacc,bestc,bestg] = SVMcgForClass(train_label,train_feature,-2,4,-4,4,3,0.5,0.5,0.9);
cmd = ['-c ',num2str(bestc),' -g ',num2str(bestg)];
 model = svmtrain(train_label,pca_train_feature, cmd);
 test_label = round(rand(1260,1)*10);
 [predicted_label,accuracy,n] = svmpredict(test_label, pca_test_feature, model,'-q');