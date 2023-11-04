clear all;

% sifra = [1 16 5 13 7 14 2 17 20 6 21 22 6; 
%          0 19 6 5 21 8 6 25 19 22 22 0 22; 
%         11 6 24 20 11 21 15 9 7 14 2 9 13;];
% 
% kluc = [14 19 24; 
%         8 20 9; 
%         13 6 15];


% sifra = [15 14 14 4 9 8 9 0 21 10 4; 
%          2 21 9 9 11 13 12 21 4 25 17 ; 
%         15 25 24 23 21 11 8 0 20 11 14 ;];
% 
% kluc = [3 8 1;
%        5 13 10; 
%        25 24 6];


sifra = [13 18 5 17 22 10 10 24 18 14; 
         12 12 9 22 21 3 24 19 21 9 ; 
         20 17 6 18 10 9 19 13 12 22 ;];

kluc = [24 21 14;
       9 19 13; 
       16 6 11];


determinant = mod(round(det(kluc)), 26);

if gcd(determinant, 26) == 1
    [~, x] = gcd(determinant, 26);
    x = mod(x, 26);
    inverznyKluc = round(mod(x * round(det(kluc)) * inv(kluc), 26), 0);
end

disp("Inverzný kľúč je ");
disp(inverznyKluc);

odhalenie = round(mod(inverznyKluc * sifra, 26), 0);
disp("Dešifrovana matica:");
disp(odhalenie);


odhalenyText = char(odhalenie + 'A');
text = reshape(odhalenyText, 1, []);
text = strrep(text, '[', 'A');
fprintf('%s\n', text);
