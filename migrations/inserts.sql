-- INSERT ACADEMIA
INSERT INTO academia (codigo_unidade, telefone, rua, cep, numero, nome, horario_abertura, horario_fechamento)
VALUES (
    1,  -- codigo_unidade
    '{"celular": "11987654321", "fixo": "1134567890"}',  -- telefone como JSONB
    'Rua da Academia',  -- rua
    '12345678',  -- cep
    '123',  -- numero
    'Academia Força é Saúde',  -- nome
    '06:00:00',  -- horario_abertura
    '22:00:00'   -- horario_fechamento
);