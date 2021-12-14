from reportlab.pdfbase.pdfdoc import PDFCatalog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3 ,landscape
from reportlab.platypus import Table
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus  import Table, Image
#from reportlab.pdfbase.ttfonts import TTfont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
# Registered font family
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
# Registered fontfamily
registerFontFamily('Vera',normal='Vera',bold='VeraBd',italic='VeraIt',boldItalic='VeraBI')



def semesterTables(data):
  roll = ""
  for roll,value in data.items():
      roll = roll
      break
  
  pdf= canvas.Canvas('output/'+roll+'.pdf', pagesize=(landscape(A3)))
  pdf.setFont('Vera',7)
  pdf.setTitle('Indian Institute of technology')
  width, height=landscape(A3)
  mainTable= Table([[''],[''],[''],['']],colWidths=410*mm,rowHeights=([25*mm,90*mm,72*mm,100*mm]))
  mainTable.setStyle([
    ('BOX',(0,0),(-1,-1),0.5,'black'),
    ('GRID',(0,0),(-1,-1),0.5,'black'),
    ('INNERGRID',(0,0),(-1,-1),1,colors.black)
    #('BOTTOMMARGIN',(0,0),(-1,-1),40),
  ])
  
  mainTable.wrapOn(pdf,width,height)
  mainTable.drawOn(pdf,5*mm,5*mm)
  imgPath='logo.jpg'
  imgwidth= width
  img=Image(imgPath,408*mm,24*mm)
  HeaderTable= Table([[img]],colWidths=([410*mm]),rowHeights=25*mm)
  HeaderTable.setStyle([
  ('BOX',(0,0),(-1,-1),0.5,'black'),
  ('GRID',(0,0),(-1,-1),0.5,'black'),
  ('LINEBEFORE',(0,0),(1,-1),1,colors.black),
  #('BOTTOMMARGIN',(0,0),(-1,-1),40),
  ])
  HeaderTable.wrapOn(pdf,width,height)
  HeaderTable.drawOn(pdf,5*mm,267*mm)

  footerTable= Table([['Date Generated : '+str(datetime.now().strftime("%Y-%m-%d %H:%M")),'Seal','Assistant Registrar']],colWidths=([160*mm,190*mm,130*mm]),rowHeights=50*mm)
  footerTable.setStyle([
    ('FONT',(-1,0),(-1,-1),'VeraBd',12),
    #('LINEABOVE',(-1,0),(-1,0),0.25,colors.black)
  ])
  footerTable.wrapOn(pdf,width,height)
  footerTable.drawOn(pdf,10*mm,60*mm)
  for key,value in data.items():
    tablex = 10
    j = 0
    tableyy = 0
    tablenameyy = 0
    changeOnce = 0
    semCount = 0
    for sub,item in value.items():
      if sub=="Overall":
        detailTable= Table([['Roll No. : '+item['1'],'Name : '+ item['2'],'Year of Admission : 20'+ item['1'][0]+item['1'][1]],['Programme : Bachelor of Technology','Course : '+item['3'],'']],colWidths=([70*mm,140*mm,70*mm]),rowHeights=([7*mm,7*mm]))
        detailTable.setStyle([
        ('BOX',(0,0),(-1,-1),0.5,'black'),
        #('GRID',(0,0),(-1,-1),0.5,'black'),
        #('LINEBEFORE',(0,0),(1,-1),1,colors.black),
        #('BOTTOMMARGIN',(0,0),(-1,-1),40),
        ])

        detailTable.wrapOn(pdf,width,height)
        detailTable.drawOn(pdf,70*mm,249*mm)
        continue
      j = j + 1
      if j <5:
        tableyy = 238
        tablenameyy = 245
      else:
        tableyy = 163
        tablenameyy = 170
        if changeOnce==0:
          tablex = 10
          changeOnce = 1
      semNameTable= Table([["Semester "+sub]],[60*mm],2*mm)
      semNameTable.setStyle([
        #('BOX',(0,0),(-1,-1),0.5,'black'),
        #('GRID',(0,0),(-1,-1),0.5,'black'),
        #('LINEBEFORE',(0,0),(1,-1),1,colors.black),
        #('BOTTOMMARGIN',(0,0),(-1,-1),40),
        ('INNERGRID',(0,0),(-1,-1),1,colors.black),
        ('FONTSIZE',(0,0),(-1,-1),7,colors.black),
        ('FONT',(0,0),(-1,0),'VeraBd',8),
        ('FONT',(-1,0),(-1,-1),'VeraBd',8),
        ('ALIGN',(0,0),(-1,-1),'LEFT'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE')
      ])

      semNameTable.wrapOn(pdf,width,height)
      semNameTable.drawOn(pdf,tablex*mm,tablenameyy*mm)  
      tempData = []
      for row in item:
        tempData.append([row[0],row[1],row[2],row[3],row[5]])
      semHeader = ['Sub Code','Subject Name','L-T-P','CRD','GRD']
      totalHeight = 0
      for i in range(0,len(tempData)):
        totalHeight = totalHeight + 4.5
      tabley = tableyy - totalHeight
      tempData.insert(0,semHeader)
      #print(tabley)
      semTable= Table(tempData,[12*mm,60*mm,9*mm,7*mm,8*mm],4.5*mm)
      semTable.setStyle([
        ('BOX',(0,0),(-1,-1),0.5,'black'),
        #('GRID',(0,0),(-1,-1),0.5,'black'),
        #('LINEBEFORE',(0,0),(1,-1),1,colors.black),
        #('BOTTOMMARGIN',(0,0),(-1,-1),40),
        ('INNERGRID',(0,0),(-1,-1),1,colors.black),
        ('FONTSIZE',(0,0),(-1,-1),7,colors.black),
        ('FONT',(0,0),(-1,0),'VeraBd',5),
        ('FONT',(-1,0),(-1,-1),'VeraBd',5),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE')
      ])

      credTaken = value["Overall"]['5'][int(sub)-1]
      credCleared = value["Overall"]['5'][int(sub)-1]
      spi = value["Overall"]['6'][int(sub)-1]
      cpi = value["Overall"]['8'][int(sub)-1]
      semTable.wrapOn(pdf,width,height)
      semTable.drawOn(pdf,tablex*mm,tabley*mm)
      semBttm = [['Credits Taken : '+str(credTaken),'Credits Cleared : '+str(credCleared),'SPI : '+str(spi),'CPI : '+str(cpi)]]
      semTableBttm= Table(semBttm,[22*mm,30*mm,14*mm,14*mm],6*mm)
      semTableBttm.setStyle([
        ('BOX',(0,0),(-1,-1),0.5,'black'),
        #('GRID',(0,0),(-1,-1),0.5,'black'),
        #('LINEBEFORE',(0,0),(1,-1),1,colors.black),
        #('BOTTOMMARGIN',(0,0),(-1,-1),40),
        #('INNERGRID',(0,0),(-1,-1),1,colors.black),
        ('FONTSIZE',(0,0),(-1,-1),7,colors.black),
        ('FONT',(0,0),(-1,-1),'VeraBd',5),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        #('FONT',(0,0),(-1,0),'VeraBd',5),
        #('FONT',(-1,0),(-1,-1),'VeraBd',5),
        #('ALIGN',(0,0),(-1,-1),'CENTER'),
        #('VALIGN',(0,0),(-1,-1),'MIDDLE')
      ])

      semTableBttm.wrapOn(pdf,width,height)
      semTableBttm.drawOn(pdf,tablex*mm,(tabley-12)*mm)
      tablex = tablex + 101
  pdf.showPage()
  pdf.save()
  print("saved",key)

      


