$i = 0
$Python = "python.exe"
$R1 = Read-Host -Prompt "Ruta en donde se encuentra el script de WebScraping"
$R2 = Read-Host -Prompt "Ruta en donde se encuentra el script de EnvioDeCorreos"
While ($i -eq 0) {
    $Destinatario = Read-Host -Prompt "Igrese la direccion a la que desa mandar el correo"
    $Yo = Read-Host -Prompt "Ingrese su correo"
    $ContraMuySegura = Read-Host -AsSecureString "Contrase�a:"
    $bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($ContraMuySegura)
    $Contrase�a = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)    
    try{
        $Contenido = &$Python $R1
        $Asunto = Read-Host -Prompt "Asunto delcorreo"
        &$Python $R2 -rmt $Yo -to $Destinatario -msg $Contenido -sub $Asunto -pwd $Contrase�a        
    } catch{
        Write-Host "No se conciguio enviar el correo"
        }
      $decision = Read-Host "Desea salir del script? [1] Si [2] No"
      if ($decision -eq "1") {
        $i = 1
      } else {
        $i = 0
      }      
  }