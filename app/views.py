from app import *


@app.route('/')
def main():
    return redirect(url_for('home'))


@app.route('/principal')
def home():
    return render_template(
        'home.html',
        lista_redes_sociais=lista_redes_sociais
    )


@app.route('/sobre')
def about():
    return render_template('about.html')


@app.route('/curriculo')
def curriculum():
    return render_template(
        'curriculum.html', 
        experiencias=lista_experiencias, 
        habilidades=lista_habilidades, 
        lista_formacoes=lista_formacoes_academicas, 
        lista_cretificados=lista_cretificados,
        lista_projetos=lista_projetos
    )

