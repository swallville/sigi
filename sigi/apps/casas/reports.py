# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from geraldo import Report, DetailBand, Label, ObjectValue, ManyElements, \
                    ReportGroup, ReportBand, landscape, SubReport, BAND_WIDTH

from sigi.apps.relatorios.reports import ReportDefault

def string_to_cm(texto):
    tamanho = 0
    minEspeciais = {
       'f':0.1,
       'i':0.05,
       'j':0.05,
       'l':0.05,
       'm':0.2,
       'r':0.1,
       't':0.15,
    }
    maiuEspeciais = {
       'I':0.05,
       'J':0.15,
       'L':0.15,
       'P':0.15,
    }
    for c in texto:
        if c > 'a' and c<'z':
            if c in minEspeciais:                
                tamanho += minEspeciais[c]                
            else:                
                tamanho += 0.17                
        else:
            if c in maiuEspeciais:                
                tamanho += maiuEspeciais[c]                
            else:                
                tamanho += 0.2                
    return tamanho



class CasasLegislativasLabels(Report):
    """
    Usage example::

      >>> from geraldo.generators import PDFGenerator
      >>> queryset = CasaLegislativa.objects.filter(municipio__uf__sigla='MG')
      >>> report = LabelsReport(queryset)
      >>> report.generate_by(PDFGenerator, filename='./inline-detail-report.pdf')

    """

    page_size = A4
    margin_top = 0.8*cm
    margin_bottom = 0.8*cm
    margin_left = 0.4*cm
    margin_right = 0.4*cm

    class band_detail(DetailBand):


        width  = 9.9*cm
        height = 5.6*cm
        margin_bottom = 0.0*cm
        margin_right  = 0.3*cm

        # With this attribute as True, the band will try to align in
        # the same line.
        display_inline = True

        default_style = {'fontName': 'Helvetica', 'fontSize': 11}


        elements = [
            Label(
                text='A Sua Excelência o(a) Senhor(a)',
                top=1*cm, left=0.5*cm, width=9.4*cm,
            ),
            ObjectValue(
                attribute_name='tipo',
                top=1.5*cm, left=0.5*cm, width=9.4*cm,
                get_value=lambda instance:
                    "Presidente da " + instance.tipo.nome + " de "
            ),
            ObjectValue(
                attribute_name='nome',
                top=2*cm, left=0.5*cm, width=9.4*cm,
                get_value=lambda instance:
                    instance.municipio.uf.nome
                        if instance.tipo.nome == u'Assembléia Legislativa'
                        else instance.municipio.nome

            ),
            ManyElements(
                ObjectValue,
                count=4,
                attribute_name=('logradouro','bairro','municipio','cep'),
                start_top=2.5*cm, height=0.5*cm, left=0.5*cm, width=9.4*cm,
            ),

        ]

class CasasLegislativasReport(ReportDefault):
    title = u'Relatório de Casas Legislativas'
    height = 80*cm

    class band_page_header(ReportDefault.band_page_header):

        label_top = ReportDefault.band_page_header.label_top
        label_left = [0.3,1,5.5,11]
        elements = list(ReportDefault.band_page_header.elements)

        elements += [
            Label(
                text="UF",
                left=label_left[0]*cm,
                top=label_top,
            ),
            Label(
                text="Municipio",
                left=label_left[1]*cm,
                top=label_top,
            ),            
            Label(
                text="Presidente",
                left=label_left[2]*cm,
                top=label_top,                
            ),
            Label(
                text="Endereço",
                left=label_left[3]*cm,
                top=label_top,                
            ),
            
        ]



    class band_page_footer(ReportDefault.band_page_footer):
        pass

    class band_detail(ReportDefault.band_detail):

        label_left = [0.3,1,5.5,11]

        elements=[
            ObjectValue(
                attribute_name='municipio.uf.sigla',
                left=label_left[0]*cm,
            ),
            ObjectValue(
                attribute_name='municipio.nome',
                left=label_left[1]*cm,
            ),            
            ObjectValue(
                attribute_name='presidente',
                left=label_left[2]*cm,
            ),
            ObjectValue(
                attribute_name='logradouro',
                left=label_left[3]*cm,
                get_value=lambda instance: instance.logradouro + ' - '+ instance.bairro,                
            ),
        ]

    groups = [
        ReportGroup(attribute_name='municipio.uf',
            band_header=ReportBand(
                height=0.7*cm,
                elements= [
                    ObjectValue(attribute_name='municipio.uf')
                ],
                borders={'top': True},
            )
        )
    ]


class CasasSemConvenioReport(CasasLegislativasReport):
    title = u'Relatório de Casas Legislativas sem Convênio'

class InfoCasaLegislativa(ReportDefault):
    title = u'Casa legislativa'
    class band_detail(ReportDefault.band_detail):
        
        posicao_left = [
            0,1.3,       #Tipo
            0,1.8,       #Regiao
            5.5,6.8,     #U.F.            
            0,2.3,       #Municipio
            0,2.4,       #Endereco
            0,1.6,       #Bairro
            0,1.3,       #CEP
            0,1.6,       #CNPJ
            0,2.3,       #Telefone
            0,2.7,       #Presidente
        ]
        posicao_top = [
            0.5,         #Tipo
            1.3,         #Regiao
            1.3,         #U.F.
            2.1,         #Municipio
            2.9,         #Logradouro
            3.7,         #Bairro
            4.5,         #CEP
            5.3,         #CNPJ
            6.1,         #Telefone
            6.9,         #Presidente
        ]

        height=30*cm

        display_inline = True        
        default_style = {'fontName': 'Helvetica', 'fontSize':14}
        
        elements = [

            Label(
                text="Tipo: ",
                left=posicao_left[0]*cm,
                top=posicao_top[0]*cm,
            ),
            ObjectValue(
                attribute_name='tipo.nome',
                left=posicao_left[1]*cm,
                top=posicao_top[0]*cm,
                width=6*cm,
            ),
            Label(
                text="Região: ",
                left=posicao_left[2]*cm,
                top=posicao_top[1]*cm,
            ),            
            ObjectValue(
                attribute_name='municipio.uf.regiao',
                left=posicao_left[3]*cm,
                top=posicao_top[1]*cm,
                get_value=lambda instance:
                      {'SL': 'Sul','SD': 'Sudeste','CO': 'Centro-Oeste','NE': 'Nordeste','NO': 'Norte',}
                      [instance.municipio.uf.regiao]
            ),
            Label(
                text="U.F.: ",
                left=posicao_left[4]*cm,
                top=posicao_top[2]*cm,
            ),
            ObjectValue(
                attribute_name='municipio.uf',
                left=posicao_left[5]*cm,
                top=posicao_top[2]*cm,
            ),                      
            Label(
                text="Município: ",
                left=posicao_left[6]*cm,
                top=posicao_top[3]*cm,
            ),
            ObjectValue(
                attribute_name='municipio.nome',
                left=posicao_left[7]*cm,
                top=posicao_top[3]*cm,
                width=20*cm,
            ),
            # Linha 3
            Label(
                text="Endereço: ",
                left=posicao_left[8]*cm,
                top=posicao_top[4]*cm,
            ),
            ObjectValue(
                attribute_name='logradouro',
                left=posicao_left[9]*cm,
                top=posicao_top[4]*cm,
                width=20*cm,
            ),
            Label(
                text="Bairro: ",
                left=posicao_left[10]*cm,
                top=posicao_top[5]*cm,
            ),
            ObjectValue(
                attribute_name='bairro',
                left=posicao_left[11]*cm,
                top=posicao_top[5]*cm,
            ),
            Label(
                text="CEP: ",
                left=posicao_left[12]*cm,
                top=posicao_top[6]*cm,
            ),
            ObjectValue(
                attribute_name='cep',
                left=posicao_left[13]*cm,
                top=posicao_top[6]*cm,
            ),
            Label(
                text="CNPJ: ",
                left=posicao_left[14]*cm,
                top=posicao_top[7]*cm,
            ),
            ObjectValue(
                attribute_name='cnpj',
                left=posicao_left[15]*cm,
                top=posicao_top[7]*cm,
            ),
            Label(
                text="Telefone: ",
                left=posicao_left[16]*cm,
                top=posicao_top[8]*cm,
            ),
            ObjectValue(
                attribute_name='telefone',
                left=posicao_left[17]*cm,
                top=posicao_top[8]*cm,
            ),
            Label(
                text="Presidente: ",
                left=posicao_left[18]*cm,
                top=posicao_top[9]*cm,
            ),
            ObjectValue(
                attribute_name='presidente',
                left=posicao_left[19]*cm,
                top=posicao_top[9]*cm,
                width=20*cm,
            ),
        ]      
    # Telefones
    tel_top = 2*cm
    tel_left = [0,3,5]
    # Contato
    cont_top = 2*cm
    cont_left = [0,6,9]
    # Convenios
    convenio_top = 2*cm
    convenio_left = [0,1.8,4.5,8,10.5,13,15.5,18]
    subreports = [
    # Telefones
        SubReport(
            queryset_string = '%(object)s.telefones.all()',
            band_header = ReportBand(
                default_style = {'fontName': 'Helvetica', 'fontSize':12    },
                height=2.5*cm,
                elements = [
                    Label(
                        text="Telefone(s)",
                        style = {'fontSize':14,'alignment': TA_CENTER},
                        width=BAND_WIDTH,
                        top=1*cm,
                    ),
                    Label(text="Número",left=tel_left[0]*cm,top=tel_top),
                    Label(text="Tipo",left=tel_left[1]*cm,top=tel_top),
                    Label(text="Nota",left=tel_left[2]*cm,top=tel_top),
                ],
                borders = {'bottom': True},
            ),
            band_detail = ReportBand(
                default_style = {'fontName': 'Helvetica', 'fontSize':11},
                height=0.5*cm,
                elements= [                    
                    ObjectValue(attribute_name='__unicode__',left=tel_left[0]*cm),
                    ObjectValue(attribute_name='tipo',left=tel_left[1]*cm,
                        get_value = lambda instance:
                            {'F':'Fixo','M':u'Móvel','X':'Fax','I':'Indefinido'}[instance.tipo],
                    ),
                    ObjectValue(attribute_name='nota',left=tel_left[2]*cm),
                ],
                borders = {'all':True},
            ),
        ),
    #Contatos
        SubReport(
            queryset_string = '%(object)s.contatos.all()',
            band_header = ReportBand(
                default_style = {'fontName': 'Helvetica', 'fontSize':12    },
                height=2.5*cm,
                elements = [
                    Label(
                        text="Contato(s)",
                        style = {'fontSize':14,'alignment': TA_CENTER},
                        width=BAND_WIDTH,
                        top=1*cm,
                    ),
                    Label(text="Nome",left=cont_left[0]*cm,top=cont_top),
                    Label(text="Nota",left=cont_left[1]*cm,top=cont_top),
                    Label(text="E-mail",left=cont_left[2]*cm,top=cont_top),
                ],
                borders = {'bottom': True,'top':True},
            ),
            band_detail = ReportBand(
                default_style = {'fontName': 'Helvetica', 'fontSize':11},
                height=0.5*cm,
                elements= [
                    ObjectValue(attribute_name='nome',left=cont_left[0]*cm),
                    ObjectValue(attribute_name='nota',left=cont_left[1]*cm),
                    ObjectValue(attribute_name='email',left=cont_left[2]*cm),
                ],
                borders = {'all':True},
            ),
        ),
    #Convenios
        SubReport(
            queryset_string = '%(object)s.convenio_set.all()',            
            band_header = ReportBand(
                     default_style = {'fontName': 'Helvetica', 'fontSize':12    },
                     height=2.5*cm,
                     elements=[
                         Label(
                             text="Convênio(s)",
                             style = {'fontSize':14,'alignment': TA_CENTER},
                             width=BAND_WIDTH,
                             top=1*cm,
                         ),
                         Label(text="Projeto",left=convenio_left[0]*cm,top=convenio_top),
                         Label(text="Nº Convenio",left=convenio_left[1]*cm,top=convenio_top),
                         Label(text="Nº Processo SF",left=convenio_left[2]*cm,top=convenio_top),
                         Label(text="Adesão",left=convenio_left[3]*cm,top=convenio_top),
                         Label(text="Convênio",left=convenio_left[4]*cm,top=convenio_top),
                         Label(text="Equipada",left=convenio_left[5]*cm,top=convenio_top),
                         Label(text="Data D.O.",left=convenio_left[6]*cm,top=convenio_top),
                     ],
                     borders = {'bottom': True}
                 ),
             band_detail = ReportBand(
                     default_style = {'fontName': 'Helvetica', 'fontSize':11},
                     height=0.5*cm,
                     elements=[
                        ObjectValue(attribute_name='projeto.sigla',left=convenio_left[0]*cm),
                        ObjectValue(attribute_name='num_convenio',left=convenio_left[1]*cm),
                        ObjectValue(attribute_name='num_processo_sf',left=convenio_left[2]*cm),
                        ObjectValue(attribute_name='data_adesao',left=convenio_left[3]*cm,
                            get_value=lambda instance:
                                instance.data_adesao.strftime('%d/%m/%Y') if instance.data_adesao != None else '-'
                        ),
                        ObjectValue(attribute_name='data_retorno_assinatura',left=convenio_left[4]*cm,
                            get_value=lambda instance:
                                instance.data_retorno_assinatura.strftime('%d/%m/%Y') if instance.data_retorno_assinatura != None else '-'
                        ),
                        ObjectValue(attribute_name='data_termo_aceite',left=convenio_left[5]*cm,
                            get_value=lambda instance:
                                instance.data_termo_aceite.strftime('%d/%m/%Y') if instance.data_termo_aceite != None else '-'
                        ),
                        ObjectValue(attribute_name='data_pub_diario',left=convenio_left[6]*cm,
                            get_value=lambda instance:
                                instance.data_pub_diario.strftime('%d/%m/%Y') if instance.data_pub_diario != None else '-'
                        ),                        
                     ],
                     borders = {'all':True},
                 ),             
        )
    ]


