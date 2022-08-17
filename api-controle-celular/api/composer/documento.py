from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import app_config
import os

class DocumentComposer:

    @classmethod
    def cria_documento(cls, funcionario):
        #Criação do Documento
        documento = Document()

        # Formatações gerais do Documento
        documento.add_picture(f'{app_config.IMG_LOCATION}/sag-dark-logo.png', width=Inches(1.71))
        estilo = documento.styles['Normal']
        fonte = estilo.font
        fonte.name = 'Arial Narrow'
        fonte.size = Pt(10)
        
        # Titulo do Documento
        titulo = documento.add_paragraph()
        titulo_format = titulo.paragraph_format
        titulo_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        titulo_run = titulo.add_run('TERMO DE RESPONSABILIDADE PARA USO DE DISPOSITIVO MÓVEL')
        titulo_run.bold = True
        titulo_font = titulo_run.font
        titulo_font.name = 'Arial Narrow'
        titulo_font.size = Pt(11)

        par_1 = documento.add_paragraph()
        par_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        run_1 = 'Pelo presente Termo de Responsabilidade para uso de dispositivo móvel, ' \
                'as partes, de um lado, '
        run_2 = f'{funcionario.nome} {funcionario.sobrenome}, '
        run_3 = 'funcionário, brasileiro, portador do RG nº '
        run_4 = f'{funcionario.rg} '
        run_5 = 'inscrito no CPF/MF sob nº '
        run_6 = '{}.{}.{}-{}, '.format(funcionario.cpf[:3], funcionario.cpf[3:6], funcionario.cpf[6:9], funcionario.cpf[9:])
        run_7 = 'doravante denominado (a) '
        run_8 = '"CONTRATADO(A)" '
        run_9 = 'e, do outro lado, SOFTWARE AG BRASIL INFORMÁTICA E SERVIÇOS LTDA., ' \
                 'sociedade brasileira, estabelecida na Cidade de São Paulo, ' \
                 'Estado de São Paulo, na Avenida das Nações Unidas, 12.901, ' \
                 'Torre Norte, 33º andar, CEP 04578-000, Brooklin Novo, ' \
                 'inscrita no Cadastro Nacional das Pessoas Jurídicas (CNPJ/MF) sob no. 07.594.862/0001-39, ' \
                 'doravante denominada “SOFTWARE AG”;'

        par_1.add_run(run_1)
        par_1.add_run(run_2).bold = True
        par_1.add_run(run_3)
        par_1.add_run(run_4).bold = True
        par_1.add_run(run_5)
        par_1.add_run(run_6).bold = True
        par_1.add_run(run_7)
        par_1.add_run(run_8).bold = True
        par_1.add_run(run_9)

        # par_1_run_1 = par_1.add_run(run_1)
        # par_1_run_1.font.name = 'Arial Narrow'
        # par_1_run_1.font.size = Pt(10)
        # par_1_run_2 = par_1.add_run(run_2, bold=True)
        # par_1_run_2.font.name = 'Arial Narrow'
        # par_1_run_2.font.size = Pt(10)
        # par_1_run_3 = par_1.add_run(run_3)
        # par_1_run_3.font.name = 'Arial Narrow'
        # par_1_run_3.font.size = Pt(10)
        # par_1_run_4 = par_1.add_run(run)




        # Salvando o Documento
        doc_path = os.path.join(app_config.UPLOAD_DOCS, f'termo_resp_{funcionario.id}.docx')
        documento.save(doc_path)

        # Abrindo o Documento para gravação local
        os.system(f'start {doc_path}')

