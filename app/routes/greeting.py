
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["Project Information"])


@router.get("/api/v1/greeting", response_class=HTMLResponse)
def greeting():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>StudyFlow AI - Project Information</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                padding: 30px 15px;
                font-family: Arial, sans-serif;
                background: #f1f5f9;
                color: #1e293b;
            }

            .container {
                max-width: 1000px;
                margin: auto;
            }

            header {
                padding: 35px;
                text-align: center;
                background: #2563eb;
                color: white;
                border-radius: 12px;
            }

            header h1 {
                margin: 0 0 12px;
                font-size: 32px;
            }

            header p {
                margin: 0;
                line-height: 1.6;
            }

            section {
                margin-top: 25px;
                padding: 25px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
            }

            h2 {
                margin-top: 0;
                color: #1d4ed8;
            }

            .status {
                display: inline-block;
                padding: 6px 12px;
                background: #dcfce7;
                color: #166534;
                border-radius: 20px;
                font-weight: bold;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 15px;
            }

            th, td {
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #e2e8f0;
            }

            th {
                background: #eff6ff;
                color: #1e40af;
            }

            code {
                padding: 3px 6px;
                background: #f1f5f9;
                border-radius: 4px;
            }

            footer {
                margin-top: 25px;
                text-align: center;
                color: #64748b;
                font-size: 14px;
            }

            @media (max-width: 650px) {
                section {
                    overflow-x: auto;
                }

                table {
                    min-width: 550px;
                }
            }
        </style>
    </head>

    <body>
        <div class="container">

            <header>
                <h1>StudyFlow AI</h1>
                <p>
                    An intelligent student task manager designed to help
                    university students organize assignments, track deadlines,
                    and plan their studies.
                </p>
            </header>

            <section>
                <h2>Project Information</h2>
                <p><strong>Project:</strong> StudyFlow AI</p>
                <p><strong>API Version:</strong> 1.0.0</p>
                <p><strong>API Status:</strong> <span class="status">Operational</span></p>
                <p><strong>Backend:</strong> Python and FastAPI</p>
            </section>

            <section>
                <h2>Team Members</h2>

                <table>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Student ID</th>
                            <th>Contribution</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr>
                            <td>Muhammadrabboni Asoev</td>
                            <td>000018849</td>
                            <td>Backend implementation, mock data, authentication,
                                CRUD endpoints, and role-based access control.</td>
                        </tr>

                        <tr>
                            <td>Nariman Huseynov</td>
                            <td>000020475</td>
                            <td>Data validation, structured responses, error handling,
                                API documentation, and example requests.</td>
                        </tr>

                        <tr>
                            <td>Emin Miftaliyev</td>
                            <td>000020362</td>
                            <td>HTML greeting endpoint, project documentation,
                                endpoint testing, and demo video preparation.</td>
                        </tr>
                    </tbody>
                </table>
            </section>

            <section>
                <h2>Available API Endpoints</h2>

                <table>
                    <thead>
                        <tr>
                            <th>Method</th>
                            <th>Endpoint</th>
                            <th>Description</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr>
                            <td>GET</td>
                            <td><code>/api/v1/greeting</code></td>
                            <td>Displays project information and API endpoints.</td>
                        </tr>

                        <tr>
                            <td>GET</td>
                            <td><code>/api/v1/assignments</code></td>
                            <td>Retrieves assignments accessible to the authenticated user.</td>
                        </tr>

                        <tr>
                            <td>GET</td>
                            <td><code>/api/v1/assignments/{id}</code></td>
                            <td>Retrieves a specific assignment.</td>
                        </tr>

                        <tr>
                            <td>POST</td>
                            <td><code>/api/v1/assignments</code></td>
                            <td>Creates a new assignment.</td>
                        </tr>

                        <tr>
                            <td>PUT</td>
                            <td><code>/api/v1/assignments/{id}</code></td>
                            <td>Updates an existing assignment.</td>
                        </tr>

                        <tr>
                            <td>DELETE</td>
                            <td><code>/api/v1/assignments/{id}</code></td>
                            <td>Deletes an assignment.</td>
                        </tr>
                    </tbody>
                </table>
            </section>

            <footer>
                StudyFlow AI API — Version 1.0.0
            </footer>

        </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)
