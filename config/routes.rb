SigmaChi::Application.routes.draw do
  get '/:action' => 'pages', :as => 'page'
  root :to => redirect('/home')
end