function [z] = ciagGeom(a0,q,n)
%funkcja liczy n podanych elementów ci¹gu
%a0 - wartoœæ pocz¹tkowa
%q - iloraz ci¹gu
%n - liczba elementów
el=a0;
for i=1:n
    fprintf('El. nr: %g = %g\n',i,el);
    el=el*q;
end

end

