from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'port': os.environ.get('PORT'),
        'service': 'linkslogic-backend-test'
    })

@app.route('/api/ask', methods=['POST'])
def ask_question():
    try:
        data = request.json
        question = data.get('question', '').strip()
        
        return jsonify({
            'success': True,
            'answer': 'Test response - OpenAI integration temporarily disabled for debugging',
            'question': question,
            'club_id': 'columbia_cc',
            'rule_type': 'test',
            'confidence': 'high',
            'response_time': 0.1
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'message': 'LinksLogic Test API - Basic Flask only', 
        'status': 'active'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f"Starting test server on port {port}")
    app.run(debug=False, host='0.0.0.0', port=port)
