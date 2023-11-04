clear all;

text = [3 7 20; 
       17 24 17; 
        0 9 0];

sifra = [13 18 5; 
         12 12 9; 
         20 17 6];


% sifra = [15 14 14;
%           2 21 9;
%          15 25 24];

% sifra = [1 16 5;
%          0 19 6;
%          11 6 24];

determinant = det(text);

inverznaMatica = inv(text);
sifrovaciaMatica = mod(round(inverznaMatica * determinant, 0),26);

klucMatice = mod(sifra * sifrovaciaMatica,26);

disp("Kľúč je:")
disp(klucMatice);

sifra = round(mod(klucMatice * text,26),0);
disp("šifra je :")
disp(sifra);
