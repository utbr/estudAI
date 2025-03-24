from django.http import HttpResponse

def main(request):
    return HttpResponse("""
        <html>
            <head>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                        text-align: center;
                    }
                    h1 {
                        font-size: 2rem;
                    }
                </style>
            </head>
            <body>
                <h1>Senhor, eu gostaria de anunciar que o projeto está no GItHub.</h1>
            </body>
        </html>
    """)
