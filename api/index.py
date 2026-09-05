"""
Vercel Serverless Function entry point for RetailIQ FastAPI application.
Exposes 'app' for Vercel Python runtime.
"""
import os
import sys

# Ensure repository root is in sys.path for Vercel serverless environment
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from backend.server import app
