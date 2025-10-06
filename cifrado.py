def main():
    cifrado = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
    mensaje=""
    letras=[]
    frecuencias=[]
    letrasFrecuentes = "eaolsndruitcpmyqbhgfvjñzxkw"
    for i in range(len(cifrado)):
        letra = cifrado[i].lower()
        if letra in letrasFrecuentes and letra not in letras:
            cont = 0
            for j in range(i, len(cifrado)):
                if letra == cifrado[j].lower():
                    cont+= 1
            pos = 0
            mayor = False
            if letras:
                while pos < len(frecuencias) and not mayor:
                    if cont > frecuencias[pos]:
                        mayor = True
                    else:
                        pos += 1
                if not mayor:
                    letras.append(letra)
                    frecuencias.append(cont)
                else:
                    letras.insert(pos, letra)
                    frecuencias.insert(pos,cont)
            else:
                letras.append(letra)
                frecuencias.append(cont)
    for i in range (len(cifrado)):
        letra = cifrado[i].lower()
        if letra in letras:
            encontrado = False
            pos = 0
            while pos < len(letras) and not encontrado:
                if letra == letras[pos]:
                    encontrado = True
                else:
                    pos += 1
            mensaje += letrasFrecuentes[pos]
        else:
            mensaje += letra
    letrasFrecuencias= dict(zip(letras,frecuencias))
    print("Letras y frecuencias:")
    print(letrasFrecuencias)
    print()
    print("Mensaje cifrado:")
    print(cifrado)
    print()
    print("Mensaje descifrado:")
    print(mensaje)
    
main()
        
        
    
                    
            
            
            
