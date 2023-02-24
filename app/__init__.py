import socket

from flask import Flask, render_template, url_for, redirect

from app.models import *

app = Flask(__name__)

