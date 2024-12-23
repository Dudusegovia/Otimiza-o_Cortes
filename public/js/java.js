
document.getElementById('executeButton').addEventListener('click', () => {
    fetch('/execute', {
        method: 'POST'
    }).then(response => {
        if (response.ok) {
            alert('Aplicativo executado e dados gravados com sucesso!');
        } else {
            alert('Erro ao executar o aplicativo.');
        }
    }).catch(error => {
        console.error('Erro:', error);
        alert('Erro ao se conectar com o servidor.');
    });
});
