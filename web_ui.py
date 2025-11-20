#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中国身份证号码验证器 - Web界面
Chinese ID Card Validator - Web Interface

基于Flask的Web界面，支持批量验证身份证号码
"""

from flask import Flask, render_template, request, jsonify
import json
from id_validator import ChineseIDValidator

app = Flask(__name__)
validator = ChineseIDValidator()

@app.route('/')
def index():
    """主页面"""
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate_ids():
    """验证身份证号码API"""
    try:
        data = request.get_json()
        input_text = data.get('input_text', '').strip()
        
        if not input_text:
            return jsonify({'error': '请输入要验证的身份证号码'}), 400
        
        # 分割成行
        lines = input_text.split('\n')
        lines = [line.strip() for line in lines if line.strip()]
        
        if not lines:
            return jsonify({'error': '请输入要验证的身份证号码'}), 400
        
        valid_ids = []
        invalid_ids = []
        
        # 逐行验证
        for line in lines:
            original_input = line
            result = validator.validate(line)
            
            if result['valid']:
                # 合法身份证
                info = result['info']
                valid_ids.append({
                    'original': original_input,
                    'processed': result['id_number'],
                    'area': info.get('area', '未知'),
                    'birth_date': info.get('birth_date', '未知'),
                    'age': info.get('age', '未知'),
                    'gender': info.get('gender', '未知')
                })
            else:
                # 不合法身份证
                invalid_ids.append({
                    'original': original_input,
                    'processed': result.get('id_number', original_input),
                    'errors': result['errors']
                })
        
        return jsonify({
            'valid_ids': valid_ids,
            'invalid_ids': invalid_ids,
            'total': len(lines),
            'valid_count': len(valid_ids),
            'invalid_count': len(invalid_ids)
        })
        
    except Exception as e:
        return jsonify({'error': f'验证过程出错: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)