%使用rgbcube展示RGB彩色立方体示意图
function rgbcube(vx,vy,vz)

%rgbcube用于展示RGB彩色立方体示意图，其中观测的角度是(vx,vy,vz)。如果无输入角度，默认为（10，10，4）.
%输入参数
vertices_matrix=[0 0 0;0 0 1;0 1 0;0 1 1;1 0 0;1 0 1;1 1 0;1 1 1];
%顶点相连构成面
faces_matrix=[1 5 6 2;1 3 7 5;1 2 4 3;2 4 8 6;3 7 8 4; 5 6 8 7];
colors=vertices_matrix;
%立方体的顶点的顺序与（r,g,b）颜色的顺序是相同的。例如（0，0，0）对应于黑色，（1，1，1）对应于白色。
%产生RGB彩色立方体示意图使用下面函数块
patch('Vertices',vertices_matrix,'Faces',faces_matrix,'FaceVertexCData',colors,'FaceColor','interp','EdgeAlpha',0)
%处理观测点
if nargin==0
    vx=10;vy=10;vz=4;
elseif nargin~=3
    error('Wrong number of inputs.')
end
axis off%取消对坐标轴的一切设置
view([2,3,3])%输入观测点
axis square%使绘图区域为正方形