%ʹ��rgbcubeչʾRGB��ɫ������ʾ��ͼ
function rgbcube(vx,vy,vz)

%rgbcube����չʾRGB��ɫ������ʾ��ͼ�����й۲�ĽǶ���(vx,vy,vz)�����������Ƕȣ�Ĭ��Ϊ��10��10��4��.
%�������
vertices_matrix=[0 0 0;0 0 1;0 1 0;0 1 1;1 0 0;1 0 1;1 1 0;1 1 1];
%��������������
faces_matrix=[1 5 6 2;1 3 7 5;1 2 4 3;2 4 8 6;3 7 8 4; 5 6 8 7];
colors=vertices_matrix;
%������Ķ����˳���루r,g,b����ɫ��˳������ͬ�ġ����磨0��0��0����Ӧ�ں�ɫ����1��1��1����Ӧ�ڰ�ɫ��
%����RGB��ɫ������ʾ��ͼʹ�����溯����
patch('Vertices',vertices_matrix,'Faces',faces_matrix,'FaceVertexCData',colors,'FaceColor','interp','EdgeAlpha',0)
%����۲��
if nargin==0
    vx=10;vy=10;vz=4;
elseif nargin~=3
    error('Wrong number of inputs.')
end
axis off%ȡ�����������һ������
view([2,3,3])%����۲��
axis square%ʹ��ͼ����Ϊ������