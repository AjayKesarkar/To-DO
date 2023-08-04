import PySimpleGUI as psg

label1 = psg.Text('Select file to compress:')
text_input1 = psg.InputText(tooltip='File to compress')
choose1 = psg.FilesBrowse('Choose')

label2 = psg.Text('Select destination folder:')
text_input2 = psg.InputText(tooltip='Destination foler')
choose2 = psg.FolderBrowse('Choose')

compress = psg.Button('Compress')

window = psg.Window('File Zipper',layout = [[label1,text_input1,choose1],[label2,text_input2,choose2],[compress]])
window.read()
window.close()