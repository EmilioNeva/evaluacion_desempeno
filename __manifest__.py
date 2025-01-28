{
    "name": "Evaluación de desempeño",
    "version": "1.0",
    "summary": "Módulo para gestionar el desempeño de los empleados",
    "category": "Productivity",
    "author": "Emilio Neva",
    "website": "https://tuweb.com",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "icon": "/evaluacion_desempeno/static/description/icon53.jpg",
    "data": [
        "views/evaluacion_desempeno_views.xml",
        "security/ir.model.access.csv"
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    "description": """
 Módulo de Odoo para la evaluación de desempeño de los empleados.
 """,
 'assets': {
        "web.assets_backend": [
            "/evaluacion_desempeno/static/src/css/styles.css"
        ],
    },
}