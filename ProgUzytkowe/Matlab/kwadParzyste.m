function [ z ] = kwadParzyste(a)
%Funkcja kt�ra generuje 
%kwadraty liczb parzystych
%a - to ilo�� tych kwadrat�w
for i = 1:a
    reszta=mod(i,2);
    if reszta == 0
        z=i*i;
        fprintf('Dla i=%d z=%d\n',i,z);
    end
end

end

