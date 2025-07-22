# limpar_python_antigo.ps1
# Execute este script no PowerShell como Administrador

Write-Host "🧼 Iniciando limpeza do PATH do sistema..." -ForegroundColor Cyan

# Defina aqui os caminhos antigos que você deseja remover:
$pathsARemover = @(
    "C:\\Program Files\\Python39\\Scripts\\",
    "C:\\Program Files\\Python39\\"
)

# Obter o PATH atual
$pathAtual = [Environment]::GetEnvironmentVariable("Path", "Machine") -split ";"

# Remover entradas antigas
$novoPath = ($pathAtual | Where-Object { $pathsARemover -notcontains $_ }) -join ";"

# Atualizar variável de ambiente do sistema
[Environment]::SetEnvironmentVariable("Path", $novoPath, "Machine")

Write-Host "✅ Entradas antigas do Python removidas com sucesso." -ForegroundColor Green

# Verificar a versão ativa do Python
Write-Host "`n🔍 Verificando versão atual do Python..." -ForegroundColor Cyan

try {
    $versaoPython = & python --version
    $caminhoPython = (Get-Command python).Source

    Write-Host "🔢 Versão ativa: $versaoPython" -ForegroundColor Yellow
    Write-Host "📂 Caminho do Python: $caminhoPython" -ForegroundColor Yellow

    if ($versaoPython -notlike "*3.13*") {
        Write-Host "`n⚠️ Atenção: a versão ativa não é a 3.13.x! Verifique se a versão desejada está instalada corretamente." -ForegroundColor Red
    } else {
        Write-Host "`n🎉 Tudo certo! Apenas a versão 3.13 está ativa." -ForegroundColor Green
    }
}
catch {
    Write-Host "❌ Erro ao executar 'python'. Verifique se ele está corretamente instalado." -ForegroundColor Red
}

Write-Host "`n💡 Reinicie seu terminal para aplicar totalmente as mudanças." -ForegroundColor Blue
