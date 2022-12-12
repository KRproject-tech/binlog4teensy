function out = load_bin( file_name, type)


fileID = fopen( file_name, 'r');
data = fread( fileID, Inf, type);

%% ���l�f�[�^�s���J�E���g
%%%
%%% �f�[�^�`��
%%% ______________________________
%%%  header            |         data          | header            |        data
%%% 0xAA 0xAA 0xAA 0xAA 0xXX 0xXX ... 0xXX 0xXX 0xAA 0xAA 0xAA 0xAA 0xXX 0xXX ...

idx = 2;
while data(idx) ~= data(1)
    data(idx)
    idx = idx + 1;
end
N_col = idx-2;    

%% ���l�f�[�^�z�񐶐�

N_data = length( data);
N_row = floor( N_data/(1 + N_col));

out = reshape( data(1:N_row*(1+N_col)).', 1+N_col, N_row).';

out = out(:,2:end);

fclose( fileID);

end