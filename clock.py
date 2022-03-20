# 闹钟子模块 url以/clock开头

from flask import Flask, render_template, request
from flask import Blueprint

clock = Blueprint('clock', __name__)


@clock.route('/')
def welcome():
    return "待写"
