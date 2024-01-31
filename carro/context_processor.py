def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        carro = request.session.get("carro", {})
        for value in carro.values():
            total = total + (float(value["precio"]))
    else:
        total = "Debes hacer login"
    return {"importe_total_carro": total}
