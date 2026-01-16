import logging
import os
from typing import Optional

from src.tools import now


def new_logger(
    name: str,
    log_dir: Optional[str] = None,
    log_file: Optional[str] = None,
    level: int = logging.INFO,
    show_console: bool = True,
) -> logging.Logger:
    """创建 logger，支持同时输出到文件和控制台"""
    logger = logging.getLogger(name)

    # 防止重复添加 handler
    if logger.handlers:
        return logger

    # ------------------------------
    #  设置统一的日志格式
    # ------------------------------
    log_format = "%(asctime)s | %(levelname)-7s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    formatter = logging.Formatter(log_format, datefmt=date_format)

    # ------------------------------
    #  文件 Handler
    # ------------------------------
    if log_dir is None:
        log_date = now().strftime("%Y-%m-%d")
        log_dir = f"tmp/logs/{log_date}"

    os.makedirs(log_dir, exist_ok=True)

    if log_file is None:
        module_name = name.split(".")[-1] if "." in name else name
        log_file = f"{module_name}.log"

    log_path = os.path.join(log_dir, log_file)

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    # ------------------------------
    #  控制台 Handler（可选）
    # ------------------------------
    if show_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # 设置 logger 整体级别
    logger.setLevel(level)

    return logger
