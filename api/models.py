class RedeSocial:
    def __init__(self, nome_rede_social: str, link: str, logo: str):
        self.nome_rede_social = nome_rede_social
        self.link = link
        self.logo = logo

    def __repr__(self) -> str:
        return f"<nome_rede_social: {self.nome_rede_social}>"


whatsapp = RedeSocial(nome_rede_social='WhatsApp',
                      link="https://api.whatsapp.com/send?phone=5565999123899&text=Olá%2C%20achei%20seu%20contato%20pelo%20portfólio%20digital.",
                      logo='./static/img/WhatsApp.png')
instagram = RedeSocial(nome_rede_social='Instagram', link='https://www.instagram.com/edimarfreitas95/',
                       logo='./static/img/Instagram.png')
linkedin = RedeSocial(nome_rede_social='LinkedIn', link='https://www.linkedin.com/in/edimar-freitas-de-sá/',
                      logo='./static/img/LinkedIn.png')
twitch = RedeSocial(nome_rede_social='Twitch', link='https://www.twitch.tv/enoisquejoga',
                    logo='./static/img/Twitch.png')
github = RedeSocial(nome_rede_social='GitHub', link='https://github.com/EdimarDeSa/', logo='./static/img/GitHub.png')

lista_redes_sociais = [whatsapp, instagram, linkedin, twitch, github]


class ExperienciaProfissional:
    def __init__(self, cargo: str, empresa: str, periodo_inicio: str, periodo_final: str, descricao: str):
        self.cargo = cargo
        self.empresa = empresa
        self.periodo_inicio = periodo_inicio
        self.periodo_final = periodo_final
        self.descricao = descricao

    def __repr__(self) -> str:
        return f'<cargo: {self.cargo}>'


analista_intelbras = ExperienciaProfissional(cargo='Analista de treinamento técnico', empresa='Intelbras',
                                             periodo_inicio='2021', periodo_final='Atual',
                                             descricao='Desenvolcimento de treinamentos técnicos sobre as técnologias da unidade de comunicação da Intelbras. Desenvolvimento de conteúdos voltados à unidaed de comunicação para Youtube.')
instrutor_intelbras = ExperienciaProfissional(cargo='Instrutor Técnico', empresa='Intelbras', periodo_inicio='2019',
                                              periodo_final='2021',
                                              descricao='Aplicação de treinamentos técnicos sobre técnologias da unidade de comunicação da Intelbras. Consultorias com revendas e integradores da Intelbras.')
autonomo_acacia = ExperienciaProfissional(cargo='Autônomo', empresa='Grupo Acácia', periodo_inicio='2018',
                                          periodo_final='2019',
                                          descricao='Trabalhei 1 ano como integrador de soluções de segurança eletrônica, soluções de redes e soluções de telefonia.')
gerente_dcol = ExperienciaProfissional(cargo='Gerente de Assistência Técnica', empresa='Dcol', periodo_inicio='2017',
                                       periodo_final='2018',
                                       descricao='Liderança da equipe de manutenção de bancada e suporte técnico em um distribuidor de equipamentos de segurança eletrônica e redes.')

lista_experiencias = [analista_intelbras, instrutor_intelbras, autonomo_acacia, gerente_dcol]


class Habilidades:
    def __init__(self, habilidades: list):
        self.habilidades = habilidades

    def __repr__(self) -> str:
        return '<lista de habilidades>'


lista_habilidades = Habilidades(
    habilidades=['Boa capacidade analítica', 'Bom senso crítico', 'Capacidade de trabalho em equipe',
                 'Boa capacidade de resolução de problemas', 'Adaptabilidade', 'Python - Django', 'Python - Flask',
                 'Python - Tkinter', 'Programação em JavaScript', 'Habilidade com CSS', 'Habilidade com HTML',
                 'Habilidade com MySQL', 'Conhecimento de aplicação de técnicas do business agility'])


class FormacaoAcademica:
    def __init__(self, curso: str, instituto: str, periodo: str) -> None:
        self.curso = curso
        self.instituto = instituto
        self.periodo = periodo

    def __repr__(self) -> str:
        return f'<curso: {self.curso}>'


graduacao = FormacaoAcademica(curso='Análise e Desenvolvimento de Sistemas', instituto='Universidade Cruzeiro do Sul',
                              periodo='02/2023 - Atualmente')
ensino_medio = FormacaoAcademica(curso='Ensino médio integrado com Eletrônica',
                                 instituto='Instituto Federal de Mato Grosso', periodo='2011 - 2015')

lista_formacoes_academicas = [graduacao, ensino_medio]


class Certificado:
    def __init__(self, curso: str, instituto: str, carga_horaria: str, link_certificado: str):
        self.curso = curso
        self.instituto = instituto
        self.carga_horaria = carga_horaria
        self.link = link_certificado

    def __repr__(self) -> str:
        return f'<curso: {self.curso}>'


python__oo = Certificado(curso='Python orientado a objetos', instituto='Alura', carga_horaria='84 horas',
                         link_certificado='https://cursos.alura.com.br/degree/certificate/34f2fe30-a72d-4584-8310-3e6b09bc4a6e')
flask = Certificado(curso='Começando com Flask', instituto='Alura', carga_horaria='21 horas',
                    link_certificado='https://cursos.alura.com.br/degree/certificate/e61b3f1b-315e-4d5a-9eea-b03aaea2da85')
modelagem_bd = Certificado(curso='Modelagem de dados', instituto='Alura', carga_horaria='39 horas',
                           link_certificado='https://cursos.alura.com.br/degree/certificate/558edea4-7b5d-481a-95ad-9af95fff217f')
todos_alura = Certificado(curso='Todos os certificados na alura', instituto='Alura', carga_horaria='',
                          link_certificado='https://cursos.alura.com.br/user/edimarfreitas95/fullCertificate/80caa8ef63a57ce4ff66306bd5b0e243')

lista_cretificados = [python__oo, flask, modelagem_bd, todos_alura]


class Projeto:
    def __init__(self, nome: str, recursos_usados: list[str]) -> None:
        self.nome = nome
        self.recursos_usados = recursos_usados

    def __repr__(self) -> str:
        return f'<nome: {self.nome}>'


gerador_bd_questao = Projeto(nome='Gerador de banco de questões',
                             recursos_usados=['Python', 'Desenvolvimento de GUI', 'Manipulação de arquivos',
                                              'Exportação para formato xlsx', 'Impressão em label printer'])
campanha_sorteio = Projeto(nome='Impressor de tickets online',
                           recursos_usados=['Python', 'JavaScript', 'Integração com APIs google Sheets',
                                            'Integração com APIs google Forms', 'Integração com APIs google Scripts'])
erp_back = Projeto(nome='ERP Back-End', recursos_usados=['Python', 'MySQL', 'Integração de Web API com MySQL',
                                                         'Preparação de ambiente linux'])
erp_front = Projeto(nome='ERP Front-End',
                    recursos_usados=['Python', 'Tkinter', 'Uso de dados através de objetos', 'Multi-Threading',
                                     'Divisão de tarefas por modulo'])

lista_projetos = [gerador_bd_questao, campanha_sorteio, erp_back, erp_front]
