function [z] = ciagGeom(a0,q,n)
%funkcja liczy n podanych element�w ci�gu
%a0 - warto�� pocz�tkowa
%q - iloraz ci�gu
%n - liczba element�w
el=a0;
for i=1:n
    fprintf('El. nr: %g = %g\n',i,el);
    el=el*q;
end

end

