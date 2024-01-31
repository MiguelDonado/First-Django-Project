from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.


def blog(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "blog/blog.html", {"posts": posts, "categorias": categorias})


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(
        request, "blog/categoria.html", {"categoria": categoria, "posts": posts}
    )
    # In this function blog defined in views.py, we can see perfectly the TVM that Django follows.
    # TVM = Template-View-Model (1.Forward, and then 2.Backward)
    # 1.[request - Views]. The user enter a url in the web browser. That match a pattern that we've defined in urls.py.
    # Then to handle the request it calls the function in views.py that we'd indicated in the urls.py for the matched pattern.
    # 2. [views - database] The function defined in views.py ask the model (database) for all categorias.
    # 3. [database - views] The model (database) return to the views function the requested values.
    # 4. [views - user] The view uses the values provided by the database and provide them as context for the template.
    # 5. [views - user] The view uses the provided path of the template to generate the response.
