import time
import logging


class HealthCheck:

    def __init__(self, checker, path):
        self.ports_checker = checker
        self.path = path

    def health_check(self):
        logging.basicConfig(filename=f'{self.path}/erros.log', level=logging.ERROR,
                            format='%(asctime)s [%(levelname)s]: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

        while True:
            try:
                opened_ports = self.ports_checker.get_opened_ports()
                missing_ports = self.ports_checker.get_missing_ports()
                logging.info(f'Portas abertas: {opened_ports}')

                if missing_ports:
                    logging.error(f'Portas faltantes: {missing_ports}')
                else:
                    logging.info('Todas as portas estão presentes na lista.')

                time.sleep(300)

            except Exception as e:
                logging.exception(f'Erro inesperado: {str(e)}')
