module.exports = {
    root: true,
    env: {
        browser: true,
        es2021: true,
        node: true,
        jest: true,
    },
    extends: [
        'airbnb',               // Estilo de Airbnb
        'plugin:prettier/recommended', // Habilita prettier + desactiva reglas conflictivas
    ],
    parserOptions: {
        ecmaVersion: 12,
        sourceType: 'module',
    },
    rules: {
        // Puedes personalizar reglas aquí:
        'react/react-in-jsx-scope': 'off', // No necesario en React 17+
        'prettier/prettier': [
            'error',
            {
                endOfLine: 'auto',
            },
        ],
        'react/jsx-filename-extension': [1, { extensions: ['.js', '.jsx'] }],
    },
};