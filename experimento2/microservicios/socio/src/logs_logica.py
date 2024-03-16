from src.socio import eventos_app, db

def escribir_log(nombre_componente, fecha_log, mensaje_log):
    
    log = eventos_app(
        nombre_componente = nombre_componente,
        fecha_log = fecha_log,
        mensaje_log = mensaje_log)
    
    db.session.add(log)
    db.session.commit()
