import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  base: '/Portafolio/',
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        tutela_viewer: resolve(__dirname, 'tutela_viewer.html'),
        tutela_video: resolve(__dirname, 'tutela_video.html'),
        reparto_viewer: resolve(__dirname, 'reparto_viewer.html'),
        reparto_video: resolve(__dirname, 'reparto_video.html'),
        procesos_viewer: resolve(__dirname, 'procesos_viewer.html'),
        procesos_video: resolve(__dirname, 'procesos_video.html'),
        notificacion_viewer: resolve(__dirname, 'notificacion_viewer.html'),
        notificacion_video: resolve(__dirname, 'notificacion_video.html'),
        actuacion_viewer: resolve(__dirname, 'actuacion_viewer.html'),
        actuacion_video: resolve(__dirname, 'actuacion_video.html'),
        anular_viewer: resolve(__dirname, 'anular_viewer.html'),
        anular_video: resolve(__dirname, 'anular_video.html'),
        gestion_viewer: resolve(__dirname, 'gestion_viewer.html'),
        gestion_video: resolve(__dirname, 'gestion_video.html'),
        tutelas2_viewer: resolve(__dirname, 'tutelas2_viewer.html'),
        tutelas2_video: resolve(__dirname, 'tutelas2_video.html')
      }
    }
  }
})
