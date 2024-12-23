const express = require('express');
const path = require('path');
const app = express();
const { exec } = require('child_process'); 
const fs = require('fs');
const PORT = 3000;

// Configura a pasta "public" como diretório de arquivos estáticos
app.use(express.static(path.join(__dirname, 'public')));

// Rota principal que serve o arquivo index.html
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
app.post('/execute', (req, res) => {
    // Substitua 'notepad.exe' pelo caminho do aplicativo que deseja executar
    exec('python.exe ./hello.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`Erro ao executar o aplicativo: ${error.message}`);
            return res.status(500).send('Erro ao executar o aplicativo.');
        }

        // Grava informações em um arquivo
        fs.writeFile('aa.txt', 'Aplicativo executado com sucesso!', (err) => {
            if (err) {
                console.error(`Erro ao gravar arquivo: ${err.message}`);
                return res.status(500).send('Erro ao gravar arquivo.');
            }

            res.send('Aplicativo executado e dados gravados com sucesso.');
        });
    });
});
// Inicia o servidor na porta definida
app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});
