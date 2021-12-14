from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 ,landscape
from reportlab.platypus import Table
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus  import Table, Image
#from reportlab.pdfbase.ttfonts import TTfont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont

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
  pdf= canvas.Canvas('output/'+roll+'.pdf', pagesize=(landscape(A4)))
  pdf.setTitle('Indian Institute of technology')
  width, height=landscape(A4)
  mainTable= Table([[''],[''],[''],['']],colWidths=289*mm,rowHeights=([20*mm,87*mm,60*mm,35*mm]))
  mainTable.setStyle([
  ('BOX',(0,0),(-1,-1),0.5,'black'),
  ('GRID',(0,0),(-1,-1),0.5,'black'),
  ('INNERGRID',(0,0),(-1,-1),1,colors.black)
  #('BOTTOMMARGIN',(0,0),(-1,-1),40),
  ])  
  mainTable.wrapOn(pdf,width,height)
  mainTable.drawOn(pdf,4*mm,4*mm)
  imgPath='logo.jpg'
  imgwidth= width
  img=Image(imgPath,288*mm,19*mm)
  HeaderTable= Table([[img]],colWidths=([287*mm]),rowHeights=19*mm)
  HeaderTable.setStyle([
  #('BOX',(0,0),(-1,-1),0.5,'black'),
  #('GRID',(0,0),(-1,-1),0.5,'black'),
  #('LINEBEFORE',(0,0),(1,-1),1,colors.black),
  #('BOTTOMMARGIN',(0,0),(-1,-1),40),
  ])  
  HeaderTable.wrapOn(pdf,width,height)
  HeaderTable.drawOn(pdf,2.4*mm,186*mm)
  for key,value in data.items():
    tablex = 7
    j = 0
    tableyy = 0
    tablenameyy = 0
    changeOnce = 0
    sem = 0
    for sub,item in value.items():
      sem = sem +1
      if sem==7:
        break
      if sub=="Overall":
        detailTable= Table([['Roll No. : '+item['1'],'Name : '+ item['2'],'Year of Admission : 20'+item['1'][0]+item['1'][1]],['Programme : Masters','Course : '+item['3'],'']],colWidths=([40*mm,60*mm,30*mm]),rowHeights=([4*mm,4*mm]))
        detailTable.setStyle([
        ('BOX',(0,0),(-1,-1),0.5,'black'),
        #('GRID',(0,0),(-1,-1),0.5,'black'),
        #('LINEBEFORE',(0,0),(1,-1),1,colors.black),
        #('BOTTOMMARGIN',(0,0),(-1,-1),40),
        ('FONT',(0,0),(-1,-1),'Vera',6),
        # ('ALIGN',(0,0),(-1,-1),'CENTER'),
        

        ])

        detailTable.wrapOn(pdf,width,height)
        detailTable.drawOn(pdf,83*mm,176*mm)
        continue
      j = j + 1
      if j <4:
        tableyy = 168
        tablenameyy = 170
      else:
        tableyy = 95
        tablenameyy = 96
        if changeOnce==0:
          tablex = 7
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
        totalHeight = totalHeight + 5
      tabley = tableyy - totalHeight
      tempData.insert(0,semHeader)
      print(tempData)
      print(tablex,tabley)
      #print(tabley)
      semTable= Table(tempData,[12*mm,50*mm,10*mm,8*mm,10*mm],4*mm)
      semTable.setStyle([
        ('BOX',(0,0),(-1,-1),0.5,'black'),
        #('GRID',(0,0),(-1,-1),0.5,'black'),
        #('LINEBEFORE',(0,0),(1,-1),1,colors.black),
        
        ('INNERGRID',(0,0),(-1,-1),1,colors.black),
        ('FONTSIZE',(0,0),(-1,-1),4,colors.black),
        ('FONT',(0,0),(-1,0),'VeraBd',6),
        ('FONT',(-1,0),(-1,1),'VeraBd',6),
         ('FONT',(0,1),(3,-1),'Vera',6),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE')
      ])

      semTable.wrapOn(pdf,width,height)
      semTable.drawOn(pdf,tablex*mm,tabley*mm)
      credTaken = value["Overall"]['5'][int(sub)-1]
      credCleared = value["Overall"]['5'][int(sub)-1]
      spi = value["Overall"]['6'][int(sub)-1]
      cpi = value["Overall"]['8'][int(sub)-1]
      semTable.wrapOn(pdf,width,height)
      semTable.drawOn(pdf,tablex*mm,tabley*mm)
      print(credTaken,credCleared,spi,cpi)
      semBttm = [['Credits Taken : '+str(credTaken),'Credits Cleared : '+str(credCleared),'SPI : '+str(spi),'CPI : '+str(cpi)]]
      semTableBttm= Table(semBttm,[25*mm,25*mm,14*mm,14*mm],3*mm)
      semTableBttm.setStyle([
        ('BOX',(0,0),(-1,-1),0.5,'black'),
        #('GRID',(0,0),(-1,-1),0.5,'black'),
        #('LINEBEFORE',(0,0),(1,-1),1,colors.black),
        #('BOTTOMMARGIN',(0,0),(-1,-1),40),
        #('INNERGRID',(0,0),(-1,-1),1,colors.black),
        ('FONTSIZE',(0,0),(-1,-1),4,colors.black),
        ('FONT',(0,0),(-1,-1),'VeraBd',6),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        #('FONT',(0,0),(-1,0),'VeraBd',5),
        #('FONT',(-1,0),(-1,-1),'VeraBd',5),
        #('ALIGN',(0,0),(-1,-1),'CENTER'),
        #('VALIGN',(0,0),(-1,-1),'MIDDLE')
      ])

      semTableBttm.wrapOn(pdf,width,height)
      semTableBttm.drawOn(pdf,tablex*mm,(tabley-6)*mm)
      tablex = tablex + 95
  pdf.showPage()
  pdf.save()






