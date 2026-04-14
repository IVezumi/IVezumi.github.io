
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random surprise:D </title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(to bottom, #015bb4, #538ebb);
        }

        .dynamic-island-button {
            position: relative;
            width: 300px;
            height: 120px;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1));
            border: 1px solid rgba(255, 255, 255, 0.5);
            border-radius: 60px;
            color: white;
            font-size: 2em;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(4, 241, 241, 0.384);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .dynamic-island-button:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(65, 105, 214, 0.349);
        }

        .dynamic-island-button::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            z-index: -1;
            border-radius: inherit;
            filter: blur(20px);
            opacity: 0.8;
            transition: opacity 0.3s ease;
        }

        .dynamic-island-button:hover::before {
            opacity: 1;
        }
    </style>
</head>
<body>
    <button class="dynamic-island-button" id="randomLinkButton">Random surprise:D</button>

    <script>
        const button = document.getElementById('randomLinkButton');
        const urls = [
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'https://www.youtube.com/watch?v=BoKQ6991WL8'
        ];

        button.addEventListener('click', () => {
            const randomIndex = Math.floor(Math.random() * urls.length);
            window.location.href = urls[randomIndex];
        });
    </script>
</body>
</html>