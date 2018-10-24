function [z] = sig(x)
if(x==0)
    z=0;
elseif(x<0)
    z=-1;
else
    z=1;
end
end

