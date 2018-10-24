function [x] = ciagArytm(a0,r,n)
%Funkcja liczaca elementy ciagu
%a0 - wyraz poczatkowy
%r - roznica
%n - liczba elementow w ciagu
el=a0;
for i=1:n
    fprintf('El. nr: %g = %g\n',i,el);
    el=el+r;
end


end

