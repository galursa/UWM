figure(1);
[x,y]=meshgrid(-pi:0.1:pi);
z=sin(x).*sin(y).*exp(-x.^2-y.^2);
mesh(x,y,z);