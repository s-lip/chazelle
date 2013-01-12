$_=("\e"x100000000)."\a";
while(s/^\e(\e{2,})/\1\a\e\1/) {}
while(s/(?<!\e)(\e+)(?!\e)(.*)\a\1+(?!\e)/\1\2/g) {}
s/\e//g;
print (length $_);
print "\n";
