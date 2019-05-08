import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as pltoff

valuess = [['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL<br>EXPENSES</b>'],
["Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad"],
[1,2,3,4,5],[1,2,3,4,5]]

trace0 = go.Table(
  columnorder = [0,1,2,3],
  columnwidth = [4,25,1,1],
  header = dict(
    values = [['<b>EXPENSES</b><br>as of July 2017'],
                  ['<b>DESCRIPTION</b>']],
    line = dict(color = '#506784'),
    fill = dict(color = 'black'),
    align = ['left','center','left'],
    font = dict(color = 'white', size = 12),
    height = 40
  ),
  cells = dict(
    values = valuess,
    line = dict(color = '#506784'),
    fill = dict(color = ['#25FEFD', 'white']),
    align = ['left', 'center'],
    font = dict(color = '#506784', size = 12),
    height = 30
    ))

data = [trace0]

pltoff.plot(data, filename = "Row and Column Size.html")
