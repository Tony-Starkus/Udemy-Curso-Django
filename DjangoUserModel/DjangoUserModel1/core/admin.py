from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')  # "autor" retorna o nome do user. "_autor" vai retornar o nome da pessoa.
    exclude = ['autor']  # Não vai mostrar o campo "autor". Isso não mostra mais um dropdown com os users.

    # instance: É a instância da classe "Post"
    def _autor(self, instance):
        return f"{instance.autor.get_full_name()}"

    # Alterar a query que consulta o BD.
    def get_queryset(self, request):
        # Vamos alterar para que a tabela no django admin mostre apenas os posts do usuário logado.
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)

    # Alterando função para pegar o ID do usuário logado para setar como autor do post.
    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)
