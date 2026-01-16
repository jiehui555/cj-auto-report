import click

from src.jobs.dev_send_daily_report import run_send_daily_report_job
from src.jobs.plm2erp_sync_reimport_sn import run_plm2erp_sync_reimport_sn_job


@click.group(help="用于执行各类自动化任务")
def cli():
    pass


@click.group(help="开发测试任务")
def dev():
    pass


@click.command(help="发送日报")
def send_daily_report():
    run_send_daily_report_job()


@click.group(help="PLM -> ERP 同步任务")
def plm2erp():
    pass


@click.command(help="重新导入料号")
def reimport_sn():
    run_plm2erp_sync_reimport_sn_job()


dev.add_command(send_daily_report)
cli.add_command(dev)

plm2erp.add_command(reimport_sn)
cli.add_command(plm2erp)
