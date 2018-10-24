%generuje wykres funkcji
figure(1);
[x,y]=meshgrid(-8:0.1:8);
z=sin(sqrt(x.^2+y.^2));
mesh(x,y,z);