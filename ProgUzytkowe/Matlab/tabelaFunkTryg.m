%Skrypt generuje tablice funkcji 
%trygonometrycznych 
%w radianach:
radiany = [0 pi/6 pi/4 pi/3 pi/2 pi]; 
sinusy = sin(radiany);
cosinusy = cos(radiany);
tangensy = tan(radiany);
cotangensy = cot(radiany);
fprintf('Sinusy\n');
disp(sinusy);
fprintf('Cosinusy\n');
disp(cosinusy);
fprintf('Tangensy\n');
disp(tangensy);
fprintf('Cotangensy\n');
disp(cotangensy);
%w stopniach
stopnie = [0 30 45 60 90 180];
sinusyst = sind(stopnie);
cosinusyst = cosd(stopnie);
tangensyst = tand(stopnie);
cotangensyst = cot(radiany);
fprintf('Sinusy\n');
disp(sinusyst);
fprintf('Cosinusy\n');
disp(cosinusyst);
fprintf('Tangensy\n');
disp(tangensyst);
fprintf('Cotangensy\n');
disp(cotangensyst);
