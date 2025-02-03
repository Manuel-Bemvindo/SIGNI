document.getElementById('gerarAcompanhamentos').addEventListener('click', function() {
    const file = document.getElementById('audioFile').files[0];
    if (!file) return alert('Selecione um arquivo de áudio.');

    const formData = new FormData();
    formData.append('audio', file);

    document.getElementById('loading').style.display = 'block';

    fetch('/processar', { method: 'POST', body: formData })
        .then(response => response.json())
        .then(data => {
            document.getElementById('loading').style.display = 'none';
            document.getElementById('audioOriginal').src = data.original;
            document.getElementById('audioAcompanhamento').src = data.acompanhamento;
            document.getElementById('audioMixado').src = data.mixado;
        });
});

document.getElementById('baixarMixado').addEventListener('click', function() {
    window.location.href = '/baixar/mixado';
});

document.getElementById('baixarAcompanhamento').addEventListener('click', function() {
    window.location.href = '/baixar/acompanhamento';
});
