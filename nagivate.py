# 导航子模块 url以/navigate开头

from flask import Flask, render_template, request
from flask import Blueprint

navigate = Blueprint('navigate', __name__)


@navigate.route('/')
def welcome():
    return "待写"
