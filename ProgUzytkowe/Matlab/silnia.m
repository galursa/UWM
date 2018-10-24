function [ z ] = silnia( n )
%Funkcja obliczajaca silnie z liczby n
%0!=1
%1!=1
%n!=(n-1)!*n
%3!=1*2*3=6
iloczyn = 1;
if (n == 0)
    z = 1;
else
    for i=1:n
        iloczyn=iloczyn*i;
    end
    z = iloczyn;
end

end

