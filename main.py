import gradio as gr

def converter(lenght1,lenght2,box1,box2):
    if (box1=='' and box2==''):
        return('Please write something to convert','Please write something to convert')
    box1=box1.replace(',','.')
    box2=box2.replace(',','.')
    if not(check_valid(box1)) and not(check_valid(box2)):
        return("Not valid","Not valid")
    if len(lenght1)!=1 and len(lenght1)!=1:
        return('Please select one unit','Please select one unit')
    elif len(lenght1)!=1:
        return('Please select one unit',box2)
    elif len(lenght2)!=1:
        return(box1,'Please select one unit')

    # elif(not(check_valid(box2))):
    #     return(box1,"Not valid")
    
    if box1!='':
        if(not(check_valid(box1))):
            return("Not valid", box2)
        n1=float(box1)
        lenght1=lenght1[0]
        lenght2=lenght2[0]
        if (lenght1=='mm' or lenght1=='cm' or lenght1=='m' or lenght1=='km' or lenght1=='in')  and (lenght2=='mm' or lenght2=='cm' or lenght2=='m' or lenght2=='km' or lenght2=='in'):
            factors = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.0, 'in':39.37}
            return(str(box1), str(n1 * (factors[lenght1] / factors[lenght2])))
        
    else:
        if(not(check_valid(box2))):
            return(box1, "Not valid")
        n1=float(box2)
        lenght1=lenght1[0]
        lenght2=lenght2[0]
        if (lenght1=='mm' or lenght1=='cm' or lenght1=='m' or lenght1=='km')  and (lenght2=='mm' or lenght2=='cm' or lenght2=='m' or lenght2=='km'):
            factors = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.0}
            return(str(n1 * factors[lenght2] / factors[lenght1]), box2)
        
        
    return("bo","bo")





def check_valid(text):
    try:
        float(text)
        return True
    except:
        return False


with gr.Blocks() as demo:
    gr.Markdown("# Unit converter")

    with gr.Row():
        with gr.Column():
            gr.Markdown('## From: ')
            lenght1=gr.CheckboxGroup(["mm", "cm", "m", "km", "in", "ft", "yd", "mi"], label="Lenght")
            box1=gr.Textbox(label="")
        with gr.Column():
            gr.Markdown('## To: ')        
            lenght2=gr.CheckboxGroup(["mm", "cm", "m", "km", "in", "ft", "yd", "mi"], label="Lenght")
            box2=gr.Textbox(label="")
    convert=gr.Button("Convert")
    convert.click(fn=converter, inputs=[lenght1,lenght2,box1,box2], outputs=[box1,box2])

demo.launch(share=False)