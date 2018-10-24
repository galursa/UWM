function [ y ] = f3(x)
%Liczy funkcjê postaci:
%      | 2 gdy x> 3
% y = {  3 gdy x=3
%      | x^2 gdy x<3
if(x==3)
    y=3;
elseif(x>3)
    y=2;
else
    y=x^2;
end

end

