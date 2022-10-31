algoritmo "Qst11Caso"

          funcao matt(x,y,z: inteiro): inteiro
                 var aux: inteiro
                 inicio
                 aux <- x * y * z
                 retorne aux
           fimfuncao

          var aluno,fim,END,matric,categ: caractere
          i,num,vld,turn,opc,curesc,cur,modl,modesc,IDD: inteiro
          CPF, ID, TEL,mat : real
          inicio
          i <- 0
          vld <- 0
             //opcoes do menu
             enquanto i <> 1 faca
                escreval("Cadastro de alunos selecione uma das opcoes: ")
                escreval(" ")
                escreval("1 -> Efetuar um novo Cadastro")
                escreval("2 -> Visualizar ultimo casdastro realizado")
                escreval("3 -> Finalizar")
                escreva("--> ")
                leia (num)
                escreval(" ")
                escolha num
                        //==> Opcao 1: parametros para preenchimento das variaveis
                        caso 1
                             //==> Validacao do numero 1 para lista de opcoes
                             escreval ("Digite 1 para as opcoes de matricula: ")
                             escreva("-> ")
                             leia(modl)
                             escreval(" ")
                             enquanto modl <> 1 faca
                                 se modl <> 1 entao
                                   escreval("Tente novamente!")
                                   escreva("-> ")
                                   leia(modl)
                                   escreval(" ")
                                 fimse
                               fimenquanto
                             escreval("Seleciona uma das opcoes:")
                             escreval(" ")
                             escreval("1 -> Presencial!")
                             escreval("2 -> EAD - Online!")
                             escreval("3 -> Flex!")
                             //==> Valida se a modalidade escolhida existe
                             escreva("-> ")
                             leia(modesc)
                             escreval(" ")
                             enquanto (modesc <> 1) e (modesc <> 2) e (modesc <> 3)  faca
                                 se (modesc <> 1) e (modesc <> 2) e (modesc <> 3) entao
                                    escreval("Selecione uma opcao valida!")
                                    escreva("-> ")
                                    leia(modesc)
                                 fimse
                             fimenquanto
                             //==> Tratativa da modalidade escolhida
                             escolha modesc
                                     caso 1
                                          escreval("Categoria Presencial escolhida!")
                                          categ <- "PS"
                                          escreval(" ")
                                     caso 2
                                          escreval("Categoria EAD - Online escolhida!")
                                          categ <- "ED"
                                          escreval(" ")
                                     caso 3
                                          escreval("Categoria Flex escolhida!")
                                          categ <- "FL"
                                          escreval(" ")
                                     fimescolha
                             //==> Parametros simples
                             escreval ("Informe o nome do aluno: ")
                             escreva("-> ")
                             leia(aluno)
                             escreval("Informe a idade do aluno: ")
                             escreva("-> ")
                             leia(IDD)
                             escreval("Informe o numero da identidade do aluno: ")
                             escreva("-> ")
                             leia(ID)
                             escreval("Informe o CPF do aluno: ")
                             escreva("-> ")
                             leia(CPF)
                             escreval("Informe o endereco do aluno: ")
                             escreva("-> ")
                             leia(END)
                             escreval("Informe o telefone do aluno: ")
                             escreva("-> ")
                             leia(TEL)
                             escreval(" ")
                             escreval("Digite 1 para ver as opcoes de cursos: ")
                             escreva("-> ")
                             leia(cur)
                             escreval(" ")
                             //==> validadacao se o numero digitado e valido
                             enquanto cur <> 1 faca
                                 se cur <> 1 entao
                                   escreval("Tente novamente!")
                                   escreva("-> ")
                                   leia(cur)
                                 fimse
                               fimenquanto
                             escreval("Seleciona uma das opcoes:")
                             escreval(" ")
                             escreval("1 -> Ciencias da Computacao!")
                             escreval("2 -> Engenharia de Softwere!")
                             escreval("3 -> Seguranca da Informacao!")
                             escreval("4 -> Direito!")
                             escreval("5 -> Medicina!")
                             escreval("6 -> Marketing!")
                             escreval("7 -> Contabilidade!")
                             escreval("8 -> Arquitetura!")
                             escreval("9 -> Engenharia!")
                             escreva("-> ")
                             leia(curesc)
                             escreval(" ")
                             //==> Tratativa para validar se a opcao digitada existe
                             enquanto (curesc <> 1) e (curesc <> 2) e (curesc <> 3) e (curesc <> 4) e (curesc <> 5) e (curesc <> 6) e (curesc <> 7) e (curesc <> 8) e (curesc <> 9) faca
                                 se (curesc <> 1) e (curesc <> 2) e (curesc <> 3) e (curesc <> 4) e (curesc <> 5) e (curesc <> 6) e (curesc <> 7) e (curesc <> 8) e (curesc <> 9) entao
                                    escreval("Selecione uma opcao valida!")
                                    escreva("-> ")
                                    leia(curesc)
                                 fimse
                             fimenquanto
                             //==> Tratativa de validacao da opcao escolhida
                             escolha curesc
                                  caso 1
                                    escreval("Curso escolhido: Ciencias da Computacao!")
                                    matric <- "CC"
                                    escreval(" ")
                                  caso 2
                                    escreval("Curso escolhido: Engenharia de Softwere!")
                                    matric <- "ES"
                                    escreval(" ")
                                  caso 3
                                    escreval("Curso escolhido: Seguranca da Informacao!")
                                    matric <- "SI"
                                    escreval(" ")
                                  caso 4
                                    escreval("Curso escolhido: Direito!")
                                    matric <- "DT"
                                    escreval(" ")
                                  caso 5
                                    escreval("Curso escolhido: Medicina!")
                                    matric <- "MD"
                                    escreval(" ")
                                  caso 6
                                    escreval("Curso escolhido: Marketing!")
                                    matric <- "MK"
                                    escreval(" ")
                                  caso 7
                                    escreval("Curso escolhido: Contabilidade!")
                                    matric <- "CB"
                                    escreval(" ")
                                  caso 8
                                    escreval("Curso escolhido: Arquitetura!")
                                    matric <- "AT"
                                    escreval(" ")
                                  caso 9
                                    escreval("Curso escolhido: Engenharia!")
                                    matric <- "EG"
                                    escreval(" ")
                             fimescolha
                             escreval("Digite 1 para ver as opcoes de turnos: ")
                             escreva("-> ")
                             leia(opc)
                             escreval(" ")
                             //==> Validacao da opcoes de turno
                               enquanto opc <> 1 faca
                                 se opc <> 1 entao
                                   escreval("Tente novamente!")
                                   leia(opc)
                                 fimse
                               fimenquanto
                               //==> Opcoes de turno
                               escreval("Seleciona uma das opcoes:")
                               escreval(" ")
                               escreval("1 -> Matutino!")
                               escreval("2 -> Vespertino!")
                               escreval("3 -> Noturno!")
                               leia(turn)
                               escreva("-> ")
                               //==> Validacao do turno escolhido
                               enquanto (turn <> 1) e (turn <> 2) e (turn <> 3) faca
                                 se (turn <> 1) e (turn <> 2) e (turn <> 3) entao
                                    escreval("Selecione uma opcao valida!")
                                    escreva("-> ")
                                    leia(turn)
                                 fimse
                               fimenquanto
                               //==> Tratativa do turno escolhido
                               escolha turn
                                  caso 1
                                    escreval("Turno Matutino!")
                                  caso 2
                                    escreval("Turno Vespertino!")
                                  caso 3
                                    escreval("Turno Noturno!")
                               fimescolha
                               //==> Validacao para formar codigo da matricula
                               vld <- vld + 1
                               mat <- matt(turn,vld,curesc)
                               escreval("Codigo da Matricula: ",mat,matric,categ)
                               escreval(" ")
                        //Visualizacao do ultimo cadastro realizado
                        caso 2
                             //valida se algum cadastro ja foi efetuado
                             se vld <> 0 entao
                              escreval("Visualizacao do cadastro")
                              escreval(" ")
                              se categ = 1 entao
                                  escreval("Matriculado na modalidade Presencial!")
                                  escreval(" ")
                              senao
                                   se categ = 2 entao
                                      escreval("Matriculado na modalidade EAD - Online!")
                                      escreval(" ")
                                   senao
                                        escreval("Matriculado na modalidade Flex")
                                        escreval(" ")
                                   fimse
                              fimse
                              escreval("Nome: ",aluno,"         Idade: ",IDD)
                              escreval("Idenidade: ",ID,"       CPF: ",CPF)
                              escreval("Endereco: ",END,"       Telefone: ",TEL)
                              escreval(" ")
                              se turn = 1 entao
                               escreval("Tuno: Matutino")
                              senao
                               se turn = 2 entao
                                escreval("Turno: Vespertino")
                               senao
                                escreval("Turno: Noturno")
                               fimse
                              fimse
                              //==> Tratativa para escrever os dados passados anteriormente
                             se curesc = 1 entao
                               escreval("Curso escolhido: Ciencias da Computacao!")
                             senao
                               se curesc = 2 entao
                                  escreval("Curso escolhido: Engenharia de Softwere!")
                               senao
                                  se curesc = 3 entao
                                    escreval("Curso escolhido: Seguranca da Informacao!")
                                  senao
                                    se curesc = 4 entao
                                      escreval("Curso escolhido: Direito!")
                                    senao
                                      se curesc = 5 entao
                                         escreval("Curso escolhido: Medicina!")
                                      senao
                                         se curesc = 6 entao
                                            escreval("Curso escolhido: Marketing!")
                                         senao
                                           se curesc = 7 entao
                                              escreval("Curso escolhido: Contabilidade!")
                                           senao
                                             se curesc = 8 entao
                                                escreval("Curso escolhido: Arquitetura!")
                                             senao
                                                escreval("Curso escolhido: Engenharia!")
                                             fimse
                                           fimse
                                         fimse
                                      fimse
                                    fimse
                                  fimse
                                fimse
                               fimse
                             escreval("Codigo da matricula: ",mat,matric,categ)
                             escreval(" ")
                             senao
                              escreval("Nenhum cadastro encontrado, o progama sera finalizado!")
                              escreval(" ")
                              interrompa
                             fimse
                        //Finalizacao do progama
                        caso 3
                             //Tratativa para finalizacao do progama
                             escreval("Digite FIM para confirmar a finalizacao do progama!")
                             escreva("--> ")
                             leia(fim)
                             enquanto fim <> "FIM" faca
                                escreval("Tente Novamente")
                                escreva("--> ")
                                leia(fim)
                             fimenquanto
                             I <- I + 1
                        outrocaso
                             escreval("Escolha uma opcao valida!")
                    fimescolha
           fimenquanto
fimalgoritmo