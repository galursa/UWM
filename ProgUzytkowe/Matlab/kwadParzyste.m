function [ z ] = kwadParzyste(a)
%Funkcja która generuje 
%kwadraty liczb parzystych
%a - to iloœæ tych kwadratów
for i = 1:a
    reszta=mod(i,2);
    if reszta == 0
        z=i*i;
        fprintf('Dla i=%d z=%d\n',i,z);
    end
end

end

